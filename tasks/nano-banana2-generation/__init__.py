#region generated meta
import typing
class Inputs(typing.TypedDict):
    prompt: str
    image_urls: list[str] | None
    num_images: int | None
    aspect_ratio: typing.Literal["auto", "21:9", "16:9", "3:2", "4:3", "5:4", "1:1", "4:5", "3:4", "2:3", "9:16"] | None
    output_format: typing.Literal["jpeg", "png", "webp"] | None
    resolution: typing.Literal["0.5K", "1K", "2K", "4K"] | None
    seed: int | None
    safety_tolerance: typing.Literal["1", "2", "3", "4", "5", "6"] | None
    limit_generations: bool | None
    enable_web_search: bool | None
class Outputs(typing.TypedDict):
    image_urls: typing.NotRequired[list[str]]
    images: typing.NotRequired[list[dict]]
#endregion

from oocana import Context
import requests
import asyncio

SUBMIT_URL = "https://fusion-api.oomol.com/v1/fal-nano-banana-2/submit"
RESULT_URL = "https://fusion-api.oomol.com/v1/fal-nano-banana-2/result/{session_id}"
POLL_INTERVAL = 5  # seconds
MAX_POLL_ATTEMPTS = 120  # 10 minutes max


async def main(params: Inputs, context: Context) -> Outputs:
    prompt = params.get("prompt", "").strip()
    if not prompt:
        raise ValueError("prompt is required and cannot be empty")

    # Get OOMOL token for authentication
    token = await context.oomol_token()
    headers = {
        "Authorization": token,
        "Content-Type": "application/json"
    }

    # Build request payload
    payload: typing.Dict[str, typing.Any] = {
        "prompt": prompt,
    }

    # Add optional parameters with defaults
    if params.get("image_urls"):
        payload["imageURLs"] = params["image_urls"]

    payload["numImages"] = params.get("num_images", 1)
    payload["aspectRatio"] = params.get("aspect_ratio", "auto")
    payload["outputFormat"] = params.get("output_format", "png")
    payload["safetyTolerance"] = params.get("safety_tolerance", "4")
    payload["resolution"] = params.get("resolution", "1K")
    payload["limitGenerations"] = params.get("limit_generations", True)

    if params.get("seed") is not None:
        payload["seed"] = params["seed"]

    if params.get("enable_web_search") is not None:
        payload["enableWebSearch"] = params["enable_web_search"]

    # Submit task
    context.report_progress(5)
    submit_response = requests.post(SUBMIT_URL, json=payload, headers=headers, timeout=60)
    submit_response.raise_for_status()
    submit_data = submit_response.json()

    if not submit_data.get("success"):
        raise ValueError(f"Failed to submit task: {submit_data}")

    session_id = submit_data.get("sessionID")
    if not session_id:
        raise ValueError("No sessionID returned from submit endpoint")

    context.report_progress(10)

    # Poll for results
    poll_url = RESULT_URL.format(session_id=session_id)
    attempts = 0

    while attempts < MAX_POLL_ATTEMPTS:
        attempts += 1
        progress = min(10 + int((attempts / MAX_POLL_ATTEMPTS) * 80), 90)
        context.report_progress(progress)

        try:
            result_response = requests.get(poll_url, headers=headers, timeout=30)
            result_response.raise_for_status()
            result_data = result_response.json()

            if not result_data.get("success"):
                # Task might still be processing, continue polling
                await asyncio.sleep(POLL_INTERVAL)
                continue

            state = result_data.get("state", "")
            
            if state == "completed":
                data = result_data.get("data", {})
                images = data.get("images", [])
                
                if not images:
                    raise ValueError("No images returned in completed task")

                image_urls = [img.get("url") for img in images if img.get("url")]
                
                if not image_urls:
                    raise ValueError("No valid image URLs in response")

                context.report_progress(100)
                
                return {
                    "image_urls": image_urls,
                    "images": images
                }
            
            elif state in ["failed", "error"]:
                error_msg = result_data.get("error", "Unknown error")
                raise ValueError(f"Task failed: {error_msg}")

            # Continue polling for other states (e.g., "processing", "pending")
            await asyncio.sleep(POLL_INTERVAL)

        except requests.exceptions.RequestException as e:
            # Network error, continue polling
            await asyncio.sleep(POLL_INTERVAL)
            continue

    raise TimeoutError(f"Task polling timed out after {MAX_POLL_ATTEMPTS * POLL_INTERVAL} seconds")
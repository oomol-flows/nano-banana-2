#region generated meta
import typing
class Inputs(typing.TypedDict):
    image_urls: list[str]
    output_format: str | None
    output_dir: str | None
class Outputs(typing.TypedDict):
    tasks: typing.NotRequired[list[dict]]
#endregion

from oocana import Context
import os

async def main(params: Inputs, context: Context) -> Outputs:
    """
    Convert image URLs to download tasks for files-downloader.
    
    Each task contains:
    - url: the image URL
    - file: the output file path (absolute path)
    """
    urls = params.get("image_urls", [])
    output_format = params.get("output_format") or "png"
    output_dir = params.get("output_dir") or context.session_dir
    
    if not urls:
        raise ValueError("No image URLs provided")
    
    # Ensure output directory exists
    os.makedirs(output_dir, exist_ok=True)
    
    tasks = []
    for i, url in enumerate(urls):
        if not url:
            continue
        
        # Generate filename with index to avoid conflicts
        filename = f"image_{i + 1}.{output_format}"
        file_path = os.path.join(output_dir, filename)
        
        tasks.append({
            "url": url,
            "file": file_path
        })
    
    if not tasks:
        raise ValueError("No valid download tasks generated")
    
    return {"tasks": tasks}
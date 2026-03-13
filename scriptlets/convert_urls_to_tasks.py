#region generated meta
import typing

class Inputs(typing.TypedDict):
    image_urls: list[str]
    output_format: str | None

class Outputs(typing.TypedDict):
    tasks: list[dict]

#endregion

from oocana import Context
import uuid

async def main(params: Inputs, context: Context) -> Outputs:
    """
    Convert image URLs to download tasks for files-downloader.
    
    Each task contains:
    - url: the image URL
    - file: the output filename (generated from URL or UUID)
    """
    urls = params.get("image_urls", [])
    output_format = params.get("output_format") or "png"
    
    if not urls:
        raise ValueError("No image URLs provided")
    
    tasks = []
    for i, url in enumerate(urls):
        if not url:
            continue
        
        # Generate filename with index to avoid conflicts
        filename = f"image_{i + 1}.{output_format}"
        
        tasks.append({
            "url": url,
            "file": filename
        })
    
    if not tasks:
        raise ValueError("No valid download tasks generated")
    
    return {"tasks": tasks}
import asyncio
import os

from dotenv import load_dotenv

load_dotenv()

import aiohttp


async def download_openapi_spec(url, token, output_file):
    headers = {
        "Authorization": f"Bearer {token}",
        'Accept': 'application/octet-stream',
    }
    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers) as response:
            response.raise_for_status()

            # Read the entire binary content of the response
            content = await response.read()

            # Open the file in binary write mode ('wb')
            with open(output_file, "wb") as file:
                file.write(content)
            print(f"File downloaded successfully to {output_file}")


async def main():
    openapi_url = "https://api.clashroyale.com/v1/#/definitions"

    # Bearer token for authentication
    token = os.getenv('clashroyale_api_key')

    # Output file for the downloaded OpenAPI spec
    openapi_file = "swagger.yaml"

    # Output directory for the generated client
    output_dir = os.getcwd()

    # Download the OpenAPI spec
    await download_openapi_spec(openapi_url, token, openapi_file)



if __name__ == "__main__":
    asyncio.run(main())

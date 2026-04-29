import os
import asyncio
from playwright.async_api import async_playwright

source_folder = input("Enter the path to the folder containing HTML files: ").strip()

if not os.path.isdir(source_folder):
    print(f"Error: The path '{source_folder}' does not exist or is not a directory.")
    exit(1)

output_folder = os.path.join(source_folder, 'exported_images')

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

async def convert_html():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        
        for filename in os.listdir(source_folder):
            if filename.lower().endswith(".html"):
                input_path = os.path.join(source_folder, filename)
                output_path = os.path.join(output_folder, filename.replace('.html', '.jpg'))
                
                print(f"Capturing: {filename}")
                
                # Convert local path to file URL
                file_url = f"file:///{os.path.abspath(input_path).replace(os.sep, '/')}"
                
                await page.goto(file_url)
                # Wait for any JS animations to finish
                await page.wait_for_timeout(1000) 
                await page.screenshot(path=output_path, type='jpeg', quality=90, full_page=True)
                
        await browser.close()
        print("All visualizations converted!")

if __name__ == "__main__":
    asyncio.run(convert_html())
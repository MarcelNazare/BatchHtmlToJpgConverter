import os
import asyncio
from playwright.async_api import async_playwright

# 1. Setup Input and Output
source_folder = input("Enter the path to the folder containing HTML files: ").strip()

if not os.path.isdir(source_folder):
    print(f"Error: The path '{source_folder}' does not exist or is not a directory.")
    exit(1)

# 2. Ask for user preference
choice = input("Convert to (1) Images [JPG] or (2) PDFs? Enter 1 or 2: ").strip()

if choice == '1':
    mode = 'image'
    extension = '.jpg'
    output_subfolder = 'exported_images'
elif choice == '2':
    mode = 'pdf'
    extension = '.pdf'
    output_subfolder = 'exported_pdfs'
else:
    print("Invalid choice. Please enter 1 or 2.")
    exit(1)

output_folder = os.path.join(source_folder, output_subfolder)
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

async def convert_files():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        
        for filename in os.listdir(source_folder):
            if filename.lower().endswith(".html"):
                input_path = os.path.join(source_folder, filename)
                output_path = os.path.join(output_folder, filename.replace('.html', extension))
                
                print(f"Processing: {filename} -> {extension}")
                
                file_url = f"file:///{os.path.abspath(input_path).replace(os.sep, '/')}"
                
                try:
                    await page.goto(file_url, wait_until="domcontentloaded", timeout=60000)
                    # Small buffer for JS/Animations
                    await page.wait_for_timeout(1000) 

                    if mode == 'image':
                        await page.screenshot(path=output_path, type='jpeg', quality=90, full_page=True)
                    else:
                        await page.pdf(
                            path=output_path, 
                            format='A4', 
                            print_background=True,
                            margin={"top": "20px", "bottom": "20px", "left": "20px", "right": "20px"}
                        )
                except Exception as e:
                    print(f"Failed to convert {filename}: {e}")
                
        await browser.close()
        print(f"\nSuccess! All files converted to {mode.upper()} format.")
        print(f"Location: {output_folder}")

if __name__ == "__main__":
    asyncio.run(convert_files())
#pip install bing-image-downloader
from bing_image_downloader import downloader

def download_lamborghini_images():
    query_string = "Audi cars"
    output_dir = "train/Audi"  # Change to your desired folder
    limit = 80  # Number of images to download
    adult_filter = True
    timeout = 60
    verbose = True

    downloader.download(query_string, limit=limit, output_dir=output_dir,
                        adult_filter_off=adult_filter, force_replace=False,
                        timeout=timeout, verbose=verbose)

if __name__ == "__main__":
    download_lamborghini_images()

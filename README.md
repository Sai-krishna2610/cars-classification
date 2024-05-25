In the **car classification** project, we classified cars based on images using the main file `car-classification.ipynb`. We utilized a pretrained VGG16 model, which was trained with ImageNet weights.

Initially, we used several scripts to scrape and download images from Google Images: `scrap.py`, `suzuki_cars_scrap.py`, `honda_cars_scrap.py`, and `mahindra_cars_scrap.py`. You can also find the dataset [here](https://drive.google.com/drive/folders/1FHyh_olwxiOql6Mc80vn7nlH71zZ-MR8?usp=sharing).

In the main project file, I split the dataset into training and testing images. Then, I imported the VGG16 pretrained model. Initially, I achieved an accuracy of 52%. After performing fine-tuning, the model's training accuracy increased to 99%, and the validation accuracy improved to 83%.

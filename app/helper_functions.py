import os, shutil

def deleteAll_fileFrom(folder_path):
    # Normalize the specified path
    # using os.path.normpath() method
    folder_path = os.path.normpath(folder_path)

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))

def resize_foto(width, height, max_width = 600):
  # max_width = in pixels. define the maximum width of the processed video.
  # the height will be proportional (defined in the calculations below)

  # if resize=True the saved video will have his size reduced ONLY IF its width is bigger than max_width
  if (width > max_width):
    # we need to make width and height proportionals (to keep the proportion of the original video) so the image doesn't look stretched
    proportion = width / height
    # to do it we need to calculate the proportion (width/height) and we'll use this value to calculate the new height
    image_width = max_width
    image_height = int(image_width / proportion)
  else:
    image_width = width
    image_height = height

  return image_width, image_height
from PIL import Image, ImageDraw

ims = []

dir_path = 'C:\\Users\\Ben\\OneDrive\\Engineering\\B1 FEM Project\\Kaye FEM2\\Anim
file_name = 'drone3_path_'
file_ext = '.png'
save_ext = '.gif'
n_frames = 43
save_name = 'drone3_paths_anim'
duration = 300

for i in range(1, n_frames+1):
    ims.append(Image.open(dir_path+'\\'+file_name+str(i)+file_ext))


ims[0].save(dir_path + '\\' + save_name + save_ext',
               save_all=True, append_images=ims[1:], optimize=False, duration=duration, loop=0)

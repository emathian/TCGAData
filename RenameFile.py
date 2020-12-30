import os 
import shutil
import re
import json

def reneme_f1():
	main_folder = "/data/gcs/tcgadata/files/DiagnosisSlides/DataExtraction_DataManagement"
	main_folder_l = os.listdir(main_folder)
	folder_TCGA_Fully_downloaded = [ 'TCGA-KICH', 'TCGA-KIRC', 'TCGA-KIRP', 'TCGA-PAAD', 'TCGA-PRAD']
	for folder in main_folder_l:
		if folder in folder_TCGA_Fully_downloaded:
			in_folder_slide_folder = os.listdir(os.path.join(main_folder, folder, folder, 'harmonized/Biospecimen/Slide_Image'))
			try:
				os.mkdir(os.path.join(main_folder, folder, "SlidesImagesRenamed"))
			except:
				print('Path : ', os.path.join(main_folder, folder, "SlidesImagesRename"), " already created."  )
			dict_OldName_NewName = dict()
			for ele in in_folder_slide_folder:
				c_slide = 0
				diagnosis_slides =  os.listdir(os.path.join(main_folder, folder, folder, 'harmonized/Biospecimen/Slide_Image', ele))
				for svsfile in diagnosis_slides:
					if svsfile.find(".svs") != -1:
						#print(" svsfile  :  ", svsfile)
						former_name = svsfile
						new_name = svsfile.split('.')[0] + '.svs'
						dict_OldName_NewName[former_name] = new_name
						shutil.move(os.path.join(main_folder, folder, folder, 'harmonized/Biospecimen/Slide_Image', ele, svsfile), os.path.join(main_folder, folder, 'SlidesImagesRenamed', new_name))

			OldName_NewName_filename = 'OldNamesNewNames_' + folder + '.txt'
			# with open(os.path.join(main_folder, folder, OldName_NewName_filename ), 'w') as file:
			# 	file.write(json.dumps(dict_OldName_NewName)) # use `json.loads` to do the reverse

def rename_f2():
	main_folder = "/data/gcs/tcgadata/files/DiagnosisSlides/DataExtraction_DataManagement"
	main_folder_l = os.listdir(main_folder)
	folder_TCGA_Fully_downloaded = [  'TCGA-KICH', 'TCGA-KIRC', 'TCGA-KIRP', 'TCGA-PAAD', 'TCGA-PRAD']
	for folder in main_folder_l:
		if folder in folder_TCGA_Fully_downloaded:
			renamed_slides_folder_l = os.listdir(os.path.join(main_folder, folder, 'SlidesImagesRenamed' ))
			for svsfolder in renamed_slides_folder_l:
				svs_slides_folder_l = os.listdir(os.path.join(main_folder, folder, 'SlidesImagesRenamed',  svsfolder))
				# rename
				for ele in svs_slides_folder_l:
					n_name = ele.split('.')[0]+'.svs'
					os.rename(os.path.join(main_folder, folder, 'SlidesImagesRenamed',  svsfolder, ele), os.path.join(main_folder, folder, 'SlidesImagesRenamed',  svsfolder, n_name) )
				# rename svs folder
				os.rename(os.path.join(main_folder, folder, 'SlidesImagesRenamed',  svsfolder) , os.path.join(main_folder, folder, 'SlidesImagesRenamed',  svsfolder + 'D'))

				# Move images
				shutil.move(os.path.join(main_folder, folder, 'SlidesImagesRenamed',  svsfolder  + 'D', n_name), os.path.join(main_folder, folder, 'SlidesImagesRenamed',  n_name))

				# Delete svs Folder
				if len(os.listdir(os.path.join(main_folder, folder, 'SlidesImagesRenamed',  svsfolder  + 'D'))) == 0:
					os.rmdir(os.path.join(main_folder, folder, 'SlidesImagesRenamed',  svsfolder  + 'D'))

reneme_f1()

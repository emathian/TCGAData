library(TCGAbiolinks)
#library(tidyverse)
# Functions ---------------------------------------------------------------
main_dir = '/data/gcs/tcgadata/files/DiagnosisSlides/DataExtraction_DataManagement'

folders = list.dirs(main_dir, full.names = FALSE ,recursive = FALSE)
Tumor.purity$CPE <- as.character(Tumor.purity$CPE)
Tumor.purity$Sample.ID <- as.character(Tumor.purity$Sample.ID)
Tumor.purity$Cancer.type <- as.character(Tumor.purity$Cancer.type)
dfTumorPurity <- data.frame(
                 sample_ID=character(), 
                 CancerType = character(),
                 CPE=character(),
                 stringsAsFactors=FALSE) 

for (folder in folders){
  if (any(grep('TCGA', folder)) == T){
    print(paste( 'folders_sample  ', folder, '\n\n'))
    folders_sample =list.dirs( paste(main_dir, folder, 'Tiles_512_512', sep = '/'), full.names = FALSE ,recursive = FALSE)
    for (sample_f in folders_sample){
      PosDash = gregexpr('-', sample_f)
      sample_ID = paste(substr(sample_f, 1, PosDash[[1]][3] -1), '01A', sep='-' )
      print(sample_ID)
      if (sample_ID %in% Tumor.purity$Sample.ID){
        CPE = Tumor.purity[Tumor.purity$Sample.ID == sample_ID, ]$CPE
        print(paste('CPE   ', CPE))
        CancerType = Tumor.purity[Tumor.purity$Sample.ID == sample_ID, ]$Cancer.type
        print(paste('Cancer type  ', CancerType))
        nrow = c(sample_ID, folder,CPE)
      }
      else{
        nrow = c(sample_ID, folder, 'NA')
      }
      dfTumorPurity = rbind( dfTumorPurity, nrow)
    }
  }
}

print(dfTumorPurity)
write.table(dfTumorPurity, file = "TCGATumorPurity.txt", append = FALSE, quote = FALSE, sep = "\t",
            eol = "\n", na = "NA", dec = ".", row.names = FALSE)

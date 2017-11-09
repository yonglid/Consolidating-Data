# Consolidating-Data
Focusing on learning to use the Pandas library for Python to consolidating and manipulate data for analysis and visualization. 

## Updating files 
This file is focused on changing the format of your current CSVs within a directory and spitting out new CSV versions in a specific directory after manipulation via dataframes. 

Command line: 
python updatingfiles_newest.py

You will be asked to pass in a path to your file directory. You can do this by typing "pwd" in terminal, in your file directory or find where your directory is. 

example: /Users/yonglidich/desktop/testdirectory

Other option from terminal is to follow the following GUI directions; 
MAC - http://osxdaily.com/2015/11/05/copy-file-path-name-text-mac-os-x-finder/

Windows - https://www.pcworld.com/article/251406/windows_tips_copy_a_file_path_show_or_hide_extensions.html

## Merge 
This file allows you to merge multiple CSVs 

python merge.py

This is already built in for updatingfiles, so you shouldn't run this separately. It's just a separate function/method to be used. 

## Scatter
This file allows for analysis of CSVs. 

python scatterplot.py

This will ask you for two file paths. One path is your first merged file (left person/right person) and second merged file (left person/right person). Both merged files were created from running updatingfiles_newest.py




3.34 : Wildcards

- for i in {1..30}; do touch file$i.txt; done :: creates files 1-30 of txts.
- ls file[1-9].txt : list files ending with 1-9 .txt
- ls file[1-9].{txt,img} : list 1-9 for both .txt and .img
- ls file{[5-9],[1][0-5]}.txt : list 5-15 of .txt
- ls *.img : list all .img files
- rm file{[1][3-9],[2][0-1]}.img : delete 13-21 of img
- : list all files, which has 3 characters long extensions starting with t



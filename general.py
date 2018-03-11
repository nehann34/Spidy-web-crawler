import os

#creating project folder

def create_project_dir(directory):
    if not os.path.exists(directory):
            print('creating directory:'+directory)
            os.makedirs(directory)


#creating queue and crawled files if not created

def create_data_files(project_name,base_url):
    queue = project_name + '/queue.txt'
    crawled = project_name + '/crawled.txt'
    if not os.path.isfile(queue):
           write_file(queue,base_url)
    if not os.path.isfile(crawled):
           write_file(crawled, '')




#create new file

def write_file(path,data):
    f=open(path,'w')
    f.write(data)
    f.close()

#we want to append further visited data to existing #file

def append_to_file(path,data):
    with open(path,'a') as file:
         file.write(data + '\n')


#deleting contents of file

def delete_file_contents(path):
    with open(path,'w'):
          pass



#for faster process use sets(unique elemts)


#read file and convert each line to set #rt=readtextfile

def file_to_set(file_name):
    results= set()
    with open(file_name,'rt') as f:
         for line in f:
             results.add(line.replace('\n',''))
    return results

#each item in set,add it to file

def set_to_file(set_name,file_name):
    delete_file_contents(file_name) 
    for links in sorted(set_name):
        append_to_file(file_name,links)
    

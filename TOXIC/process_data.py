import csv

def process_document(f='test_nat_mod.csv'):

    data = []
    labels = []

    improper_count = 0

    with open(f,'r', encoding="latin1") as fh:
        reader_1 = csv.reader(fh,delimiter=',')
        for row in reader_1:
            comment_id = row[0]
            #import pdb;pdb.set_trace()
            hour = row[4].split(' ')[-1].split(':')[0]        
            month = row[4].split(' ')[0].split('-')[1]
            comment = row[1].strip().lower()
            comment_parent = row[7].strip().lower()
            author = row[3].strip().lower()
            label = row[-4]

            comment_data = comment

            if label == '100':
                improper_count+=1

            if label in ['100','105']:
                data.append(comment_data)
                labels.append(label)


    new_data = []
    new_labels = []

    for k,comment in enumerate(data):
        if labels[k] == '100':
            new_data.append(comment)
            #new_labels.append(labels[k])
            new_labels.append(0)
        elif labels[k] == '105' and len(new_data) < improper_count:
            new_data.append(comment)
            #new_labels.append(labels[k])
            new_labels.append(1)

    return [new_data, new_labels]
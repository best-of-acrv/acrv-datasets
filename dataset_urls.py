"""This file contains all supported datasets. To add a new dataset, create a new url dictionary with corresponding keys (dataset name)
and values (urls):

e.g. new_dataset_urls = {'newdataset2014' : 'http://example.com/file2014.zip',
                         'newdataset2017' : 'http://example.com/file2017.zip'}

Then, add a new line to the get_urls function below. E.g. for the above example:

elif dataset == 'newdataset':
       return new_dataset_urls
"""

# dataset names and URLS
nyu_urls = {'nyu' : 'https://cloudstor.aarnet.edu.au/plus/s/XkNRzW15f5TCDKr/download'}
voc_urls = {'voc' : 'http://host.robots.ox.ac.uk/pascal/VOC/voc2012/VOCtrainval_11-May-2012.tar'}
sbd_urls = {'sbd' : 'http://www.eecs.berkeley.edu/Research/Projects/CS/vision/grouping/semantic_contours/benchmark.tgz'}
coco_urls = {'coco_train2014' : 'http://images.cocodataset.org/zips/train2014.zip',
             'coco_val2014' : 'http://images.cocodataset.org/zips/val2014.zip',
             'coco_annotations_trainval2014' : 'http://images.cocodataset.org/annotations/annotations_trainval2014.zip',
             'coco_test2015' : 'http://images.cocodataset.org/zips/test2015.zip',
             'coco_train2017' : 'http://images.cocodataset.org/zips/train2017.zip',
             'coco_val2017' : 'http://images.cocodataset.org/zips/val2017.zip',
             'coco_annotations_trainval2017' : 'http://images.cocodataset.org/annotations/annotations_trainval2017.zip',
             'coco_captions' : 'https://cloudstor.aarnet.edu.au/plus/s/4rQwvU3VuTd5U7d/download',
             'coco_vqa_questions_train' : 'https://s3.amazonaws.com/cvmlp/vqa/mscoco/vqa/v2_Questions_Train_mscoco.zip',
             'coco_vqa_questions_val' : 'https://s3.amazonaws.com/cvmlp/vqa/mscoco/vqa/v2_Questions_Val_mscoco.zip',
             'coco_vqa_questions_test' : 'https://s3.amazonaws.com/cvmlp/vqa/mscoco/vqa/v2_Questions_Test_mscoco.zip',
             'coco_vqa_annotations_train' : 'https://s3.amazonaws.com/cvmlp/vqa/mscoco/vqa/v2_Annotations_Train_mscoco.zip',
             'coco_vqa_annotations_val' : 'https://s3.amazonaws.com/cvmlp/vqa/mscoco/vqa/v2_Annotations_Val_mscoco.zip'}
glove_urls = {'glove' : 'http://nlp.stanford.edu/data/glove.6B.zip'}
trainval36_urls = {'trainval36' : 'https://cloudstor.aarnet.edu.au/plus/s/bE4nMgkvejbbJMl/download'}
# add new datasets with URLS here

def get_urls(dataset):
    if dataset == 'nyu':
        return nyu_urls
    elif dataset == 'voc':
        return voc_urls
    elif dataset == 'sbd':
        return sbd_urls
    elif dataset == 'coco':
        return coco_urls
    elif dataset == 'glove':
        return glove_urls
    elif dataset == 'trainval36':
        return trainval36_urls
    else:
        print('Invalid dataset selected : please check that --dataset chooses from [nyu, voc, sbd, coco, glove, trainval36] ')
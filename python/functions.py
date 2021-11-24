import json, datetime
from matplotlib import pyplot as plt

def print_traffic(highlight, leng):
    for i, (left, right) in enumerate(highlight):
        print('['+str(i+1)+'] ' + str(datetime.timedelta(seconds=int(left))) + ' ~ ' +
        str(datetime.timedelta(seconds=int(right))))
    print("Number of highlights: %d" % len(highlight))
    print("Full length of highlight: %dmin %dsec" % (leng//60, leng%60))


def visualization(x, path):
    x.plot(figsize=(50, 15), grid=True, title="Catch Highlights")
    plt.xlabel("sec")
    plt.savefig(path)


def return_json(return_data, path):
    with open(path, 'w') as outfile:
        json.dump(return_data, outfile)
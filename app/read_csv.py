import csv

def read_csv(path):
  with open(path, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter = ',')
#delimiter is the char that separates the elements of the csv file
    header = next(reader)
    #print(header)
    data = []
    for row in reader:
      iterable = zip(header, row)
#Creates a tuple with the header (first value) and the row (second value)
      #print(list(iterable))
      country_dict = {key: value for key, value in iterable} #Dictionary comprehension
      data.append(country_dict)
    return data
      #print('***' * 5)
      #print(row)

if __name__ == '__main__':
  data = read_csv('./app/data.csv')
#print(data[0])
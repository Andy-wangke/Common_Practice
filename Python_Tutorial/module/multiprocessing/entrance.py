from multiprocessing import Pool

def f(x):
    return x*x

pages =10
for page in range(1,int(pages)+1):
    print(page)

car_info = []
car_links = [1,2,3,4,5]
#
[car_info.append(car_link) for car_link in car_links]
print(car_info)


if __name__=='__main__':
    with Pool(5) as p:
        print(p.map(f,[1,2,3,4,5]))
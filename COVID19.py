import json

with open("covid_19.json") as c:
    data = json.load(c)

global dates, confirmed_cases_week

dates= []
confirmed_cases_week=[]
cd=[]


def confimed_cases_eachday(i):
    confirmed_cases = 0
    death_cases = 0
    recovered_cases = 0
    for key, value in data.items():
        for index in range(len(value)):
            if index == i:
                confirmed_cases += value[index]["confirmed"]
                death_cases += value[index]["deaths"]
                recovered_cases += value[index]["recovered"]
    confirmed_cases_week.append(confirmed_cases)
    return confirmed_cases, death_cases, recovered_cases

def max_num_eachday(i):
    maximum_num = 0
    max_country = ""
    date = ""
    for key, value in data.items():
        for index in range(len(value)):
            if index == i:
                if (maximum_num < value[index]["confirmed"]):
                    maximum_num = value[index]["confirmed"]
                    max_country = key
                    date = dates[i]
    return max_country,date,maximum_num


def weekly_cases():
    total_weekly_cases=0
    for i in range(0, len(confirmed_cases_week), 7):
        cc = (confirmed_cases_week[i:i + 7])
        cd.append(cc)
    for n in range(len(cd)):
        print("Confirmed cases in week ", n + 1, " are: ", sum(cd[n]))

    return total_weekly_cases



for j in range(len(data["Thailand"])):
  f=data["Thailand"][j]["date"]
  dates.append(f)

for i in range(len(data["Thailand"])):
    d=confimed_cases_eachday(i)
    print("On Date ", dates[i], " :--> ", "\n Confirmed Cases:", d[0], "\n Deaths : ", d[1],
          "\n Recovered Cases: ", d[2])
    print("*******************************")
    m=max_num_eachday(i)
    print("Maximum number of cases in ", m[0], "On ", m[1], "are", m[2])
    print("######################################################")


wc=weekly_cases()

# for i in range(len(data["Thailand"])):
#     w=weekly_confimed_cases(i)
# print(confirmed_cases_week)






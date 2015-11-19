import gradeData
import csv

def print_csv(data):
    with open('grade_data.csv','wb') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=',')
        csvwriter.writerow(["Term Code", "Subject Code", "Course Code", "Course Title", "Instructor", "GPA", "Percent A", "Percent B", "Percent C", "Percent D", "Percent F", "Percent Dropped with a W", "Percent P", "Percent NP"])
        for i in range(len(data)):
            csvwriter.writerow([data[i].term_code,data[i].sub_code,data[i].cor_code,data[i].cor_title,data[i].inst,data[i].gpa,data[i].perc_a,data[i].perc_b,data[i].perc_c,data[i].perc_d,data[i].perc_f,data[i].perc_w,data[i].perc_p,data[i].perc_np])

grade_data = gradeData.build_grade_data()
print_csv(grade_data)

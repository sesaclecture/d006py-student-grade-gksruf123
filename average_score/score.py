#염한결 - 학생 성적 고지 개인 과제입니다!

#!/usr/bin/env python
import sys
import csv


def load_from_csv(filepath):
    """
    Read students' names and scores from given 
    csv file and return it in dict with list of subjects.
    """
    student_scores = {}

    with open(filepath, 'r', encoding='utf-8') as f:
        csv_reader = csv.reader(f)

        # Readout the header
        # 이름, 국어, 수학, 영어, 과학, 사회
        header = next(csv_reader)

        for row in csv_reader:
            student_scores[row[0]] = row[1:]
    return student_scores, header[1:]

student_scores, subjects = load_from_csv("score.csv")

subjects_avg = {"국어": 0, "수학": 0, "영어": 0, "과학": 0, "사회": 0}  #과목 평균 딕셔너리

def avg_score_cal(subject, num):    
    total_score = 0
    for i in student_scores:
        score = int(student_scores[i][num-1])
        total_score += score
    avg_score = total_score / len(student_scores)
    subjects_avg[subject] = avg_score
    return subjects_avg


def subject_average_cal():
    """
    이 반의 각 과목별 평균을 구해서 딕셔너리로 반환
    예) {"국어": 80.8, "수학": 35.3, "영어": 96.6, "과학": 85.3, "사회": 38.8}
    """
    avg_score_cal("국어", 1)
    avg_score_cal("수학", 2)
    avg_score_cal("영어", 3)
    avg_score_cal("과학", 4)
    avg_score_cal("사회", 5)
    return subjects_avg

subject_average_cal()
# print(subjects_avg)

personal_avg_score = []     #학생별 전과목 평균 점수 들어 있는 튜플 리스트

def student_average():
    """
    각 학생별 전과목 평균 점수를 정렬된 튜플의 리스트로 반환
    예) [("이영희", 89.8), ("김철수", 86.6), ("박민수", 84.8)]
    """
    #평균 구하기
    
    personal_total_score = 0
    for student_name in student_scores:
        personal_total_score = sum(int(score) for score in student_scores[student_name])
        avg_score = personal_total_score / len(subjects)
        personal_avg_score.append((student_name, avg_score))

student_average()

final_result = sorted(personal_avg_score, key=lambda x: x[1], reverse=True)     #학생별 평균 점수 높은 순으로 정렬한 튜플 리스트

print("과목 평균:")
for sub, avg in subjects_avg.items():
    print(f"\t{sub}: {avg:.2f}")

print("학생 점수:")
for avg in final_result:
    print(f"\t{avg[0]}: {avg[1]:.2f}")

def analyze_result(name: str, roll: int, marks: list) -> None:
    total = sum(marks)
    average = total / len(marks) if marks else 0.0
    
    if average >= 90:
        grade = "A"
    elif average >= 75:
        grade = "B"
    elif average >= 60:
        grade = "C"
    elif average >= 40:
        grade = "D"
    else:
        grade = "Fail"
        
    print(f"Student: {name} (Roll: {roll})")
    print(f"Total: {total:.1f}, Average: {average:.1f}")
    print(f"Grade: {grade}")
    
    below_40 = []
    for idx, mark in enumerate(marks, start=1):
        if mark < 40:
            below_40.append(f"Subject {idx}")
            
    if below_40:
        print(f"Subjects below 40: {', '.join(below_40)}")


if __name__ == "__main__":
    name = "Aarav"
    roll = 101
    marks = [88.5, 35.0, 76.0, 92.5, 48.0]
    
    analyze_result(name, roll, marks)

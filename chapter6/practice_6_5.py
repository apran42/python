# def profile(name, age, lang1, lang2, lang3, lang4, lang5):
#     print(f"이름 : {name}\t나이 : {age}\t", end=" ")  # end=" " : 줄 바꿈 없이 출력
#     print(lang1, lang2, lang3, lang4, lang5)

def profile(name, age, *language):
    print(f"이름 : {name}\t나이 : {age}\t", end=" ")
    for lang in language:
        print(lang, end=" ")
    print()


profile("유재석", 20, "Python", "Java", "C", "C++", "C#", "JavaScript")
profile("김태호", 25, "Kotlin", "Swift")

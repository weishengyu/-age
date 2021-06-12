drving = input('請問你有沒有開過車？')
if drving != '有' and drving != '沒有':
	print('只能輸入有或沒有')
	raise SystemExit

age = input('請問你的年齡？')
age = int(age)
if drving == '有':
	if age >= 18:
		print('你通過測驗了')
	else:
		print('奇怪你怎麼會開過車')
elif drving == '沒有':
	if age >= 18:
		print('你可以去考駕照了趕快去考')
	else:
		print('很好過幾年就可以考了')


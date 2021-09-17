has_high_income = True
has_good_credit = True

if has_high_income and has_good_credit:
    print("1) Eligible for loan")
if has_high_income or has_good_credit:
    print("2) Eligible for loan")
if has_high_income and not has_good_credit:
    print("3) Eligible for loan")

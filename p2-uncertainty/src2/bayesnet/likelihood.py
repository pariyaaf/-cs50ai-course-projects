from model import model

# نگاشت رشته‌ها به ایندکس‌های عددی
mapping = {
    "none":    0,
    "light":   1,
    "heavy":   2,
    "yes":     0,
    "no":      1,
    "on time": 0,
    "delayed": 1,
    "attend":  0,
    "miss":    1
}

def main():
    # ۱) تعریف مشاهده به صورت رشته‌ای
    obs_str = ["none", "no", "on time", "attend"]
    # ۲) تبدیل به لیست اعداد: [[rain, maintenance, train, appointment]]
    obs_idx = [[ mapping[state] for state in obs_str ]]
    # ۳) محاسبه احتمال
    prob = model.probability(obs_idx)
    # ۴) نمایش خروجی
    print("Observation indices:", obs_idx)
    print("Probability:", float(prob))

if __name__ == "__main__":
    main()

from pomegranate.distributions import Categorical, ConditionalCategorical
from pomegranate.bayesian_network import BayesianNetwork

# 1) بارش (rain) — سه حالت: none, light, heavy
d_rain = Categorical([[0.7, 0.2, 0.1]])

# 2) نگهداری (maintenance) شرطی بر rain
#    هر سطر باید یک شیء Categorical باشد
d_maintenance = ConditionalCategorical([
    Categorical([[0.4, 0.6]]),   # rain = none
    Categorical([[0.2, 0.8]]),   # rain = light
    Categorical([[0.1, 0.9]]),   # rain = heavy
])

# 3) حرکت قطار (train) شرطی بر (rain, maintenance)
#    هر ترکیب از والدین باید یک شیء Categorical باشد
d_train = ConditionalCategorical([
    # rain = none
    Categorical([[0.8, 0.2]]),  # maintenance = yes
    Categorical([[0.9, 0.1]]),  # maintenance = no
    # rain = light
    Categorical([[0.6, 0.4]]),  # maintenance = yes
    Categorical([[0.7, 0.3]]),  # maintenance = no
    # rain = heavy
    Categorical([[0.4, 0.6]]),  # maintenance = yes
    Categorical([[0.5, 0.5]]),  # maintenance = no
])

# 4) قرار (appointment) شرطی بر train
d_appointment = ConditionalCategorical([
    Categorical([[0.9, 0.1]]),  # train = on time
    Categorical([[0.6, 0.4]]),  # train = delayed
])

# 5) ساخت شبکهٔ بیزی: لیست توزیع‌ها و لیست یال‌ها
model = BayesianNetwork(
    [d_rain, d_maintenance, d_train, d_appointment],
    [
        (d_rain,        d_maintenance),
        (d_rain,        d_train),
        (d_maintenance, d_train),
        (d_train,       d_appointment),
    ],
    # نام گره‌ها برای خوانایی بهتر (اختیاری ولی توصیه می‌شود)
    names=["rain", "maintenance", "train", "appointment"]
)

# تعریف حالت‌های هر متغیر برای نگاشت صحیح
# این کار باعث می‌شود نیازی به فایل mapping جداگانه در likelihood.py نباشد
model.bake()
model.states_by_name['rain'].keys = ["none", "light", "heavy"]
model.states_by_name['maintenance'].keys = ["yes", "no"]
model.states_by_name['train'].keys = ["on time", "delayed"]
model.states_by_name['appointment'].keys = ["attend", "miss"]
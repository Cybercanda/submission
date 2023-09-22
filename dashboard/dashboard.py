import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency
sns.set(style='whitegrid')

st.header('Dashbord Submission Kelas Data Analyst :sparkles:')
st.text('Create: Bily Hakim Erlangga')

# Dataset
days_df = pd.read_csv("data/day.csv")
hours_df = pd.read_csv("data/hour.csv")

# Hitung jumlah pengguna berdasarkan kolom "workingday" dan "Holiday" dengan data days
user_count_workingday = days_df['workingday'].value_counts()
user_count_holiday = days_df['holiday'].value_counts()
# Hitung jumlah pengguna berdasarkan kolom "workingday" dan "Holiday" dengan data hours
user_count_workinghour = hours_df['workingday'].value_counts()
user_count_holihour = hours_df['holiday'].value_counts()

# Jumlahkan pengguna berdasarkan kolom "workingday" dan "Holiday" dengan data days
total_users_workingday = user_count_workingday.sum()
total_users_holiday = user_count_holiday.sum()
# Jumlahkan pengguna berdasarkan kolom "workingday" dan "Holiday" dengan data hours
total_users_workinghour = user_count_workinghour.sum()
total_users_holihour = user_count_holihour.sum()

# Buat aplikasi web Streamlit
st.subheader('Data Pengguna Data (Day)')

# Dataset Day
col1, col2 = st.columns(2)

with col1:
    # Tampilkan diagram barplot untuk 'workingday'
    st.metric("Persebaran Data Pengguna Kolom workingday", value=total_users_workingday)
    fig, ax = plt.subplots()
    sns.barplot(x=user_count_workingday.index, y=user_count_workingday.values, ax=ax)
    ax.set_xlabel('workingday')
    ax.set_ylabel('Jumlah Pengguna')
    st.pyplot(fig)

with col2:
    # Tampilkan diagram barplot untuk 'holiday'
    st.metric("Persebaran Data Pengguna Kolom holiday", value=total_users_holiday)
    fig, ax = plt.subplots()
    sns.barplot(x=user_count_holiday.index, y=user_count_holiday.values, ax=ax)
    ax.set_xlabel('holiday')
    ax.set_ylabel('Jumlah Pengguna')
    st.pyplot(fig)

# Dataset Hour
st.subheader('Data Pengguna Data (Hour)')
col1, col2 = st.columns(2)

with col1:
    # Tampilkan diagram barplot untuk 'workingday'
    st.metric("Persebaran Data Pengguna Kolom workingday", value=total_users_workinghour)
    fig, ax = plt.subplots()
    sns.barplot(x=user_count_workingday.index, y=user_count_workingday.values, ax=ax)
    ax.set_xlabel('workinghour')
    ax.set_ylabel('Jumlah Pengguna')
    st.pyplot(fig)

with col2:
    # Tampilkan diagram barplot untuk 'holiday'
    st.metric("Persebaran Data Pengguna Kolom holiday", value=total_users_holihour)
    fig, ax = plt.subplots()
    sns.barplot(x=user_count_holiday.index, y=user_count_holiday.values, ax=ax)
    ax.set_xlabel('holihour')
    ax.set_ylabel('Jumlah Pengguna')
    st.pyplot(fig)

# Bagian Rental Sepeda
# Dataset days
st.markdown("---")
st.subheader("Jumlah Rental Sepeda (Day)")

rental_count_workingdays = days_df.groupby("workingday")["cnt"].sum()
rental_count_holiday = days_df.groupby("holiday")["cnt"].sum()
rental_count_workinghour = hours_df.groupby("workingday")["cnt"].sum()
rental_count_holihour = hours_df.groupby("holiday")["cnt"].sum()

total_rental_workingday = rental_count_workingdays.sum()
total_rental_holiday = rental_count_holiday.sum()
total_rental_workinghour = rental_count_workinghour.sum()
total_rental_holihour = rental_count_holihour.sum()

col1, col2 = st.columns(2)

with col1:
    # Tampilkan diagram barplot untuk 'workingday'
    st.metric("Persebaran Data jumlah rental Kolom workingday", value=total_rental_workingday)
    fig, ax = plt.subplots()
    sns.barplot(x=user_count_workingday.index, y=user_count_workingday.values, ax=ax)
    ax.set_xlabel('workingday')
    ax.set_ylabel('Jumlah Rental')
    st.pyplot(fig)

with col2:
    # Tampilkan diagram barplot untuk 'holiday'
    st.metric("Persebaran Data Pengguna Kolom holiday", value=total_rental_holiday)
    fig, ax = plt.subplots()
    sns.barplot(x=user_count_holiday.index, y=user_count_holiday.values, ax=ax)
    ax.set_xlabel('holiday')
    ax.set_ylabel('Jumlah Rental')
    st.pyplot(fig)

st.subheader("Jumlah Rental Sepeda (Hour)")
col1, col2 = st.columns(2)

with col1:
    # Tampilkan diagram barplot untuk 'workingday'
    st.metric("Persebaran Data jumlah rental Kolom workingday", value=total_rental_workinghour)
    fig, ax = plt.subplots()
    sns.barplot(x=user_count_workingday.index, y=user_count_workingday.values, ax=ax)
    ax.set_xlabel('workingday')
    ax.set_ylabel('Jumlah Rental')
    st.pyplot(fig)

with col2:
    # Tampilkan diagram barplot untuk 'holiday'
    st.metric("Persebaran Data Pengguna Kolom holiday", value=total_rental_holihour)
    fig, ax = plt.subplots()
    sns.barplot(x=user_count_holiday.index, y=user_count_holiday.values, ax=ax)
    ax.set_xlabel('holiday')
    ax.set_ylabel('Jumlah Rental')
    st.pyplot(fig)

# Cuaca
rental_wetherdays = days_df.groupby("weathersit")["cnt"].sum()
weatherhours = hours_df.groupby("weathersit")["cnt"].sum()

st.markdown("---")
st.subheader("Persebaran Rental Bike berdasarkan Cuaca")
# Pie chart untuk workingday
fig1, ax1 = plt.subplots()
ax1.pie(rental_wetherdays, labels=rental_wetherdays.index, autopct='%1.1f%%', startangle=90)
ax1.set_title('Data Day')
st.pyplot(fig1)

# Pie chart untuk weatherhours
fig2, ax2 = plt.subplots()
ax2.pie(weatherhours, labels=weatherhours.index, autopct='%1.1f%%', startangle=90)
ax2.set_title('Data Hours')
st.pyplot(fig2)

st.subheader('Conclusion')
st.markdown('- conclution pertanyaan 1 = Saya menentukan variabel jumlah pengguna dan jumlah rental sepeda. Dengan masing-masing diambil dari data days dan hours, walaupun saya bisa mengambil salah satu dataset saja, namun saya ingin memperkaya informasi. Untuk data days, bisa dilihat bahwa jumlah pengguna pada hari kerja jauh lebih banyak dibandingkan hari weekend atau holidays. Lalu, rental sepeda yang dilakukan pada hari kerja juga memiliki intensitas yang tinggi dibandingkan dengan hari sebaliknya. Saya juga menggunakan kolom holidays, walaupun saya tau ini tidak berimbang karena jumlah holidays sangat sedikit yang akan menimbulkan bias, tetapi dilihat dari persebaran data. Baik jumlah pengguna dan jumlah rental sepeda memiliki intensitas yang rendah pada hari libur. Lalu, hasil yang sama juga dilalui untuk data hours. Yakni perseberan data dengan jumlah pengguna dan jumlah penyewaan sepeda memiliki intensitas yang tinggi pada hari kerja dibandingkan sebaliknya.')
st.markdown('- conclution pertanyaan 2 = Saya menjawab pertanyaan kedua dengan menghitung jumnlah total pengguna berdasarkan cuaca. Untuk data pada dataset days, total penyewaan sepeda terbanyak berturut-turut yakni, pada cuaca cerah (1) sebanyak 66.6%, lalu kabut + mendung (2) sebanyak 30.3% dan terakhir salju ringan sebesar 1.2%. Tidak ada pengguna yang menyewa pada cuaca Hujan Lebat + Hujan ES + Badai Petir + Kabut (4). Lalu untuk data pada dataset hours, tidak terlalu berbeda jauh dari komposisinya, yang pertama pada cuaca cerah (1) sebesar 71.0%, lalu kabut + mendung (2) sebesar 24.2%, kemudian salju ringan (3) 4.8% dan terakhir cuaca Hujan Lebat + Hujan ES + Badai Petir + Kabut sebesar 0,06%.'
            'Notes:'
            'Nomor pada kesimpulan pertanyaan kedua, merujuk kepada karakteristik cuaca yang disediakan dataset.')
import streamlit as st
import preprocessor,helper
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="WhatsApp Chat Analyzer", page_icon="💬", layout="wide", initial_sidebar_state="collapsed")

st.markdown(
    """
    <style>
    .stApp {
        background: radial-gradient(circle at 20% 20%, #f8f5ef 0%, #f4efe4 40%, #efe6d6 100%);
        color: #111111;
    }
    [data-testid="stAppViewContainer"],
    [data-testid="stAppViewContainer"] p,
    [data-testid="stAppViewContainer"] label,
    [data-testid="stAppViewContainer"] span,
    [data-testid="stAppViewContainer"] div {
        color: #111111;
    }
    .main .block-container {
        padding-bottom: 4.5rem;
    }
    section.main {
        overflow: visible !important;
    }
    .hero {
        background: linear-gradient(120deg, #0f766e 0%, #1f2937 100%);
        border-radius: 18px;
        padding: 1.2rem 1.4rem;
        margin-bottom: 1rem;
        color: #f8fafc;
        box-shadow: 0 10px 24px rgba(0,0,0,0.15);
    }
    .hero h1 {
        margin: 0;
        font-size: 2rem;
        letter-spacing: 0.3px;
    }
    .hero p {
        margin: 0.35rem 0 0 0;
        color: #e2e8f0;
        font-size: 1rem;
    }
    .section-title {
        margin: 0.4rem 0 0.8rem 0;
        font-size: 2rem;
        font-weight: 800;
        letter-spacing: 0.6px;
        text-transform: lowercase;
        color: #102a43;
        text-shadow: 0 2px 10px rgba(15, 118, 110, 0.18);
    }
    [data-testid="stAppViewContainer"] [data-testid="stMetricLabel"] p {
        color: #334155 !important;
        font-weight: 600;
    }
    [data-testid="stAppViewContainer"] [data-testid="stMetricValue"] {
        color: #0f172a !important;
    }
    [data-testid="stAppViewContainer"] h3 {
        color: #0f172a !important;
    }
    [data-testid="stSidebar"],
    [data-testid="collapsedControl"] {
        display: none !important;
    }
    .controls {
        background: rgba(255, 255, 255, 0.65);
        border: 1px solid rgba(15, 23, 42, 0.08);
        border-radius: 14px;
        padding: 0.9rem 1rem;
        margin-bottom: 1rem;
    }
    [data-testid="stFileUploader"] label,
    [data-testid="stFileUploader"] small,
    [data-testid="stFileUploader"] span,
    [data-testid="stFileUploader"] p {
        color: #111111 !important;
    }
    [data-testid="stFileUploaderDropzone"] {
        background: #f8fafc !important;
        border: 1px dashed #94a3b8 !important;
    }
    [data-testid="stFileUploaderDropzone"] * {
        color: #0f172a !important;
    }
    [data-testid="stFileUploader"] button {
        background: #0f172a !important;
        color: #f8fafc !important;
        border: 1px solid #0f172a !important;
    }
    [data-testid="stFileUploader"] button:hover {
        background: #1e293b !important;
        border-color: #1e293b !important;
    }
    .footer {
        position: fixed;
        left: 0;
        width: 100vw;
        max-width: 100vw;
        bottom: 0;
        z-index: 999;
        padding: 0.7rem 0;
        margin: 0 !important;
        text-align: center;
        font-size: 0.95rem;
        color: #1e293b;
        background: rgba(248, 245, 239, 0.92);
        backdrop-filter: blur(3px);
        border-top: 1px solid rgba(15, 23, 42, 0.22);
    }
        div[data-baseweb="select"] > div {
            background: #f8fafc !important;
            color: #111111 !important;
            border: 1px solid #94a3b8 !important;
        }
        div[data-baseweb="select"] span,
        div[data-baseweb="select"] svg {
            color: #111111 !important;
            fill: #111111 !important;
        }
        .stButton > button {
            background: #0f766e !important;
            color: #ffffff !important;
            border: 1px solid #0f766e !important;
            font-weight: 600;
        }
        .stButton > button:hover {
            background: #0d9488 !important;
            border-color: #0d9488 !important;
            color: #ffffff !important;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="hero">
        <h1>WhatsApp Chat Analyzer</h1>
        <p>Turn your chat export into beautiful timelines, activity insights, and language patterns.</p>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown('<div class="controls"><b>Upload and Controls</b></div>', unsafe_allow_html=True)

#now to upload file
uploaded_file=st.file_uploader("Choose a chat file", type=["txt"])
if uploaded_file is not None:
    bytes_data=uploaded_file.getvalue()
    data=bytes_data.decode("utf-8")#covert into string
    #st.text(data)  #to print this text data
    df=preprocessor.preprocess(data)#preprocessor ek library bnYI JHA preprocess func present h vha se call kr liya

    #Debug: Show first few rows and data shape
    st.info(f"Data loaded: {len(df)} messages found")
    if len(df) == 0:
        st.error("No messages were parsed from the file. Please make sure your WhatsApp chat is in the correct format: DD/MM/YYYY, HH:MM - Name: Message")
    #st.dataframe(df)#function to distplay dataframe

     #fetch unique users
    user_list=df['user'].unique().tolist()
    if 'group_notification' in user_list:
        user_list.remove('group_notification')#group notification hta rhe
    user_list.sort()#list sort kr rhe
    user_list.insert(0,"overall")#0th pos pe overall add kr rhe
    selected_user=st.selectbox("Show analysis for",user_list)#.selectbox(label, options): Creates a dropdown menu (select box)
    #adding button
    if st.button("Show analysis", use_container_width=True):#when button click it will run
        #stats area
        st.markdown('<div class="section-title">Top Statistics</div>', unsafe_allow_html=True)

        num_messages,num_words,num_media,num_links=helper.fetch_stats(selected_user,df)
        
        col1,col2,col3,col4=st.columns(4)#st.columns(4): Creates four columns in the Streamlit layout.col1, col2, col3, col4 are variables representing each column.
        
        with col1:#Ensures the content inside is placed in the first column.
            st.metric("Total Messages", num_messages)
        with col2:
            st.metric("Total Words", num_words)
        with col3:
            st.metric("Media Shared", num_media)
        with col4:
            st.metric("Links Shared", num_links)
        
        #monthly timeline
        st.markdown("### Monthly Timeline")
        timeline=helper.monthly_timeline(selected_user,df)
        fig,ax=plt.subplots()
        ax.plot(timeline['time'],timeline['message'],color="#0f766e", linewidth=2.5)
        ax.set_facecolor("#fffdf8")
        plt.xticks(rotation="vertical")
        st.pyplot(fig)

        #daily timeline
        st.markdown("### Daily Timeline")
        daily_timeline=helper.daily_timeline(selected_user,df)
        fig,ax=plt.subplots()
        ax.plot(daily_timeline['only_date'],daily_timeline['message'],color="#be185d", linewidth=2.2)
        ax.set_facecolor("#fffdf8")
        plt.xticks(rotation="vertical")
        st.pyplot(fig)


        #activity map
        st.markdown("### Activity Map")
        col1,col2=st.columns(2)
        with col1:
            st.subheader("Most Busy Day")
            busy_day=helper.week_activity_map(selected_user,df)
            fig,ax=plt.subplots()
            ax.bar(busy_day.index,busy_day.values, color="#2563eb")
            ax.set_facecolor("#fffdf8")
            plt.xticks(rotation="vertical")
            st.pyplot(fig)

        with col2:
            st.subheader("Most Busy Month")
            busy_month=helper.month_activity_map(selected_user,df)
            fig,ax=plt.subplots()
            ax.bar(busy_month.index,busy_month.values,color="#ea580c")
            ax.set_facecolor("#fffdf8")
            plt.xticks(rotation="vertical")
            st.pyplot(fig)

        st.markdown("### Weekly Activity Heatmap")
        user_heatmap=helper.activity_heatmap(selected_user,df)
        if not user_heatmap.empty and user_heatmap.shape[0] > 0 and user_heatmap.shape[1] > 0:
            fig,ax=plt.subplots()
            ax=sns.heatmap(user_heatmap, cmap="YlGnBu")
            st.pyplot(fig)
        else:
            st.write("No activity data available for heatmap")

        #finding the busiest users in the group(group level)
        if selected_user=="overall":
          st.markdown("### Most Busy Users")
          x,new_df=helper.most_busy_users(df)#yha se dataframe aa gya ki unique users aur kitte mssgs h in descending order
          fig,ax=plt.subplots()#use to create multiple plots in same fig vo yad h na 4 bnata tha basically syntax hota [plt.subplot(rows, columns, index)] no. of rows, no. of columns aur kon sa vla plot...# baki whatsapp wle jupiter wle me dekh lo
          col1,col2=st.columns(2)#basically poore area ko 2 part me divide kr rhe 1 side hm log bar chart plot krege top 5 users ka aur dusre side hr user ne kitta % chat kiya overall
          
          with col1:
              ax.bar(x.index,x.values,color="#dc2626")
              ax.set_facecolor("#fffdf8")
              plt.xticks(rotation="vertical")
              st.pyplot(fig)
          with col2:
              st.dataframe(new_df)#to show df

        #worldcloud
        st.markdown("### Wordcloud")
        df_wc=helper.create_wordcloud(selected_user,df)
        if df_wc is not None:
            fig,ax=plt.subplots()
            ax.imshow(df_wc)#imshow is for image display
            st.pyplot(fig)
        else:
            st.write("Not enough words to generate wordcloud")

        #most common words
        st.markdown("### Most Common Words")
        most_common_df=helper.most_common_words(selected_user,df)
        if not most_common_df.empty:
            fig,ax=plt.subplots()
            ax.barh(most_common_df[0],most_common_df[1], color="#0ea5e9")#0 or 1 isliye kyuki st.dataframe(most_common_df) ye krne pe unke col ke nam 0 aur 1 bn rhe
            #barh means horizontal barchart
            plt.xticks(rotation="vertical")
            st.pyplot(fig)
        else:
            st.write("No common words found")


        #emoji analysis
        st.markdown("### Emoji Analysis")
        emoji_df=helper.emoji_helper(selected_user,df)
        if not emoji_df.empty:
            col1,col2=st.columns(2)
            with col1:
               st.dataframe(emoji_df)
            with col2:
                fig,ax=plt.subplots()
                ax.pie(emoji_df[1],labels=emoji_df[0],autopct="%0.2f")#autopct shows how much % of each slice...% is a placeholder for a number.....0.2f specifies that the number should be formatted as a floating-point value with 2 decimal places.e.g 25% =25.00
                st.pyplot(fig)
        else:
            st.write("No emojis found")

        #time based analysis

st.markdown('<div class="footer">Made with ❤️ by Nirbhay</div>', unsafe_allow_html=True)
        




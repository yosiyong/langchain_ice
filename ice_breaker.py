from langchain.prompts import  PromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os
from third_parties.linkedin import scrape_linkedin_profile

if __name__ == "__main__":
    load_dotenv()
    print("hello langchain")

summary_template = """
    given the Linkedin information {information} about a person from I want you to create:
    1. a short summary
    2. two interesting facts about them
"""

summary_prompt_template = PromptTemplate(
    input_variables=["information"], template=summary_template
)

llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")

# chain作成
chain = summary_prompt_template | llm

# linkedinからプロフィルデータ取得(mock=True:APIを使わず、固定のmockファイルを取得する)
linkedin_data = scrape_linkedin_profile(linkedin_profile_url="https://www.linkedin.com/in/eden-marco/",mock=True)
res = chain.invoke(input={"information": linkedin_data})
# chain実行
print(res)
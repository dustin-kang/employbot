from fastapi import FastAPI, Body, Request, APIRouter
import json

from SlackAPI import *
import slack_tokens

router = APIRouter(
    prefix="/search",
)

@router.post("/total")
async def search_job():
    slack_client = SlackAPI(token=slack_tokens.SLACK_APP_TOKEN)
    blocks = [
		{
			"dispatch_action": True,
			"type": "input",
			"element": {
				"type": "plain_text_input",
				"action_id": "plain_text_input-action",
				"placeholder": {
					"type": "plain_text",
					"text": "파이썬 신입"
				}
			},
			"label": {
				"type": "plain_text",
				"text": "기업명, 공고명등 검색해보세요.",
				"emoji": True
			}
		}
	]
    result = slack_client.post_message(channel_id=slack_tokens.CHANNEL_ID, text="직업검색", blocks=blocks)
    return 


@router.post("/interactive")
async def get_job(request: Request):
    form_data = await request.form()
    payload = json.loads(form_data.get("payload"))
    query=payload["actions"][0]['value']
    slack_client = SlackAPI(token=slack_tokens.SLACK_APP_TOKEN)
    if query == None:
        result = slack_client.post_message(channel_id=slack_tokens.CHANNEL_ID, text="아무것도 입력하지 않았습니다.")
        return
    else:
        query = query.replace(" ", "%20")
        texts = f"""
		💡 관련 직무를 찾아보세요.
		잡코리아 : https://www.jobkorea.co.kr/OnePick/JobList?Keyword={query}
		원티드 : https://www.wanted.co.kr/search?query={query}
		사람인 : https://www.saramin.co.kr/zf_user/search?searchword={query}
		"""
        result = slack_client.post_message(channel_id=slack_tokens.CHANNEL_ID, text=texts)
        return 
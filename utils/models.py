"""Model Initialization File

Configures the LLM model used throughout the workshop notebook.

Default: OpenAI (gpt-5.4) for the main agent. The research subagent in Part 4
of the notebook uses gpt-5.4-mini. Both come from the OPENAI_API_KEY in `.env`.

═══════════════════════════════════════════════════════════════════════════
  ⚠  IMPORTANT: install the matching extra BEFORE swapping providers
═══════════════════════════════════════════════════════════════════════════

  Provider              Install command              Already installed?
  --------------------  ---------------------------  ---------------------
  OpenAI (default)      -                            yes (default dep)
  Anthropic             -                            yes (default dep)
  Azure OpenAI          uv sync --extra azure        no - install first
  AWS Bedrock           uv sync --extra bedrock      no - install first
  Google Vertex/Gemini  uv sync --extra google       no - install first

═══════════════════════════════════════════════════════════════════════════

To swap providers:
  1. Run the install command above (if needed).
  2. Comment out the Default Models section below.
  3. Uncomment the section for your desired provider.
  4. Set the provider's env vars in `.env` (see notes inline).
"""

from pathlib import Path
from dotenv import load_dotenv

# Anchor the .env path to the repo root (utils/ -> repo root is one level up)
# so the model works regardless of the cwd the script is launched from.
load_dotenv(dotenv_path=Path(__file__).resolve().parent.parent / ".env", override=True)

from langchain.chat_models import init_chat_model


# ---- Default Models -------------------------------------------------------
# Workshop default: OpenAI GPT-5.4 for the main agent.
# Requires OPENAI_API_KEY in .env
model = init_chat_model("openai:gpt-5.4")
sub_agent_model = init_chat_model("openai:gpt-5.4-mini")

# model = init_chat_model("anthropic:claude-haiku-4-5")
# sub_agent_model = init_chat_model("anthropic:claude-haiku-4-5")


# ---- Azure OpenAI Using Environment Variables ---------------------------------------------------------
# Install first:  uv sync --extra azure
# You need to have the OPENAI_API_KEY and AZURE_OPENAI_ENDPOINT 
# environment variables.
# from langchain_openai import AzureChatOpenAI

# model = AzureChatOpenAI(
#     azure_deployment="gpt-5.4",
#     api_version="2024-12-01-preview"
# )

# sub_agent_model = model = AzureChatOpenAI(
#     azure_deployment="gpt-5.4",
#     api_version="2024-12-01-preview"
# )

# ---- Azure OpenAI: Using Azure AD ---------------------------------------------------------
# from azure.identity import InteractiveBrowserCredential

# credential = InteractiveBrowserCredential()

# def get_token():
#     token = credential.get_token("https://cognitiveservices.azure.com/.default")
#     return token.token

# model = AzureChatOpenAI(
#     api_version="2024-03-01-preview",
#     azure_endpoint="https://deployment.openai.azure.com/",
#     azure_deployment="gpt-5.4",
#     azure_ad_token_provider=get_token,
# )


# ---- AWS Bedrock ----------------------------------------------------------
# import os
# from langchain_aws import ChatBedrockConverse

# AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
# AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
# AWS_REGION_NAME = os.getenv("AWS_REGION_NAME")
# AWS_MODEL_ARN = os.getenv("AWS_MODEL_ARN")

# model = ChatBedrockConverse(
#     aws_access_key_id=AWS_ACCESS_KEY_ID,
#     aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
#     region_name=AWS_REGION_NAME,
#     provider="anthropic",
#     model_id=AWS_MODEL_ARN,
# )


# ---- Google Vertex AI -----------------------------------------------------
# Make sure your Vertex AI credentials are set up and GOOGLE_APPLICATION_CREDENTIALS
# points to the JSON file.

# import os
# from pathlib import Path
# from langchain.chat_models import init_chat_model

# # Resolve project root and load .env (utils/ -> project root is one level up)
# project_root = Path(__file__).resolve().parent.parent
# load_dotenv(dotenv_path=project_root / ".env", override=True)

# # Make the credentials path absolute if it was given as a relative path
# if "GOOGLE_APPLICATION_CREDENTIALS" in os.environ:
#     cred_path = os.environ["GOOGLE_APPLICATION_CREDENTIALS"]
#     if not os.path.isabs(cred_path):
#         os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = str(project_root / cred_path.lstrip("./"))

# model = init_chat_model("google_vertexai:gemini-2.5-flash")

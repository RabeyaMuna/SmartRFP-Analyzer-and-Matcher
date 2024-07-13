from fastapi import APIRouter, FastAPI, HTTPException, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from azure.storage.blob.aio import BlobServiceClient
from pydantic import BaseModel
from data_model.llm.llm import fn_rag_infer


router = APIRouter()


# # Define the model for signup request
# class LLMResult(BaseModel):
#     id: str
#     llm_prediction_summarize: str
#     llm_prediction_title: str
#     llm_prediction_vendor: str
#     llm_prediction_client: str
#     llm_prediction_Date: str
#     llm_prediction_scope: str
#     llm_prediction_about: str
#     llm_prediction_Resouces: str
#     llm_prediction_Domain: str
#     llm_prediction_Deliverables: str
#     llm_prediction_designations: str
#     llm_prediction_skill: str
#     llm_prediction_Outcome: str


# Define a route for making predictions
@router.post('/predict')
async def predict(llm_result: LLMResult):


    llm_prediction_summarize = fn_rag_infer("summarize")
    # print("llm_prediction_summarize: ", llm_prediction_summarize)

    # fn_rag_infer("---")
    llm_prediction_title=fn_rag_infer("title")
    # print("llm_prediction_title: ", llm_prediction_title)

    llm_prediction_vendor=fn_rag_infer("vendor company")
    # print("llm_prediction_vendor: ", llm_prediction_vendor)

    llm_prediction_client=fn_rag_infer("client company")
    # print("llm_prediction_client: ", llm_prediction_client)

    llm_prediction_Date=fn_rag_infer("Date")
    # print("llm_prediction_Date: ", llm_prediction_Date)

    # fn_rag_infer("---")
    # llm_prediction_summarizefn_rag_infer("summarize")
    llm_prediction_scope=fn_rag_infer("Brief summary of the scope")
    # print("llm_prediction_scope: ", llm_prediction_scope)

    # fn_rag_infer("---")
    llm_prediction_about=fn_rag_infer("project about") 
    # print("llm_prediction_about: ", llm_prediction_about)
    
    llm_prediction_Resouces=fn_rag_infer("Resouces Required")
    # print("llm_prediction_Resouces: ", llm_prediction_Resouces)

    llm_prediction_Domain=fn_rag_infer("Domain/Field of the Proposal")
    # print("llm_prediction_Domain: ", llm_prediction_Domain)

    # fn_rag_infer("---")
    llm_prediction_Deliverables=fn_rag_infer("Deliverables")
    # print("llm_prediction_Deliverables: ", llm_prediction_Deliverables)

    llm_prediction_designations=fn_rag_infer("job tittles and role/designations")
    # print("llm_prediction_designations: ", llm_prediction_designations)

    llm_prediction_skill=fn_rag_infer("List of skill tags included")
    # print("llm_prediction_skill: ", llm_prediction_skill)

    # fn_rag_infer("---")
    llm_prediction_Outcome=fn_rag_infer("Outcome")
    # print("llm_prediction_Outcome: ", llm_prediction_Outcome)

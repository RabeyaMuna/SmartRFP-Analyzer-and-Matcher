from fastapi import APIRouter, FastAPI, HTTPException, UploadFile, File
from azure.storage.blob.aio import BlobServiceClient
from data_model import file_result_methods
from data_model.llm.llm import fn_rag_infer
from azure.storage.blob.aio import BlobServiceClient
from fastapi import UploadFile, HTTPException
from azure.core.exceptions import ResourceExistsError
import time
import os

load_dotenv()

router = APIRouter()

# Upload file endpoint
@router.post("/uploadfile_single")
async def create_upload_file(file: UploadFile = File(...)):
    name = file.filename

    start_upload = time.time()
    upload_response = await upload_to_azure(file, name)
    end_upload = time.time()

    upload_time = end_upload - start_upload

    if isinstance(upload_response, HTTPException):
        raise upload_response
    
    start_predict = time.time()
    prediction_results = await predict(name)
    end_predict = time.time()

    predict_time = end_predict - start_predict

    return {"upload_status": upload_response, "prediction_results": prediction_results, "upload_time_seconds": upload_time, "prediction_time_seconds": predict_time}


async def upload_to_azure(file: UploadFile, file_name: str):
    connect_str = os.getenv('AZURE_BLOB_CONNECTOR')
    blob_service_client = BlobServiceClient.from_connection_string(connect_str)
    container_name = os.getenv('AZURE_BLOB_CONTAINER')
    
    async with blob_service_client:
        container_client = blob_service_client.get_container_client(container_name)
        try:
            blob_client = container_client.get_blob_client(file_name)
            f = await file.read()
            await blob_client.upload_blob(f)

        except Exception as e:
            if isinstance(e, ResourceExistsError):
                return HTTPException(409, "Blob with the same name already exists...")
            else:
                print(e)
                return HTTPException(401, "Something went terribly wrong..")
    
    return {"upload_to_azure": "success"}


# Predict function
async def predict(blob_name):
    llm_file_name = blob_name
    llm_prediction_title = fn_rag_infer("RFP project title", blob_name)
    llm_prediction_Date = fn_rag_infer("RFP file Date", blob_name)
    llm_prediction_vendor = fn_rag_infer("RFP project vendor/service company", blob_name)
    llm_prediction_client = fn_rag_infer("RFP project client/customer", blob_name)
    llm_prediction_about = fn_rag_infer("RFP project about", blob_name)
    llm_prediction_summarize = fn_rag_infer("RFP project summarization", blob_name)
    llm_prediction_scope = fn_rag_infer("RFP project scope", blob_name)
    llm_prediction_Domain = fn_rag_infer("Domain/Field of the RFP Proposal", blob_name)
    llm_prediction_Resouces = fn_rag_infer("RFP project's Resouces Required", blob_name)
    llm_prediction_Deliverables = fn_rag_infer("RFP project's Deliverables", blob_name)
    llm_prediction_designations = fn_rag_infer("job tittles and role/designations required for the project", blob_name)
    llm_prediction_skill = fn_rag_infer("skill required for the RFP project", blob_name)
    llm_prediction_Outcome = fn_rag_infer("Outcome of the RFP project", blob_name)
    
    predictions = {
        "file_name": llm_file_name,
        "title": llm_prediction_title,
        "Date": llm_prediction_Date,
        "vendor": llm_prediction_vendor,
        "client": llm_prediction_client,
        "about": llm_prediction_about,
        "summarize": llm_prediction_summarize,
        "scope": llm_prediction_scope,
        "Domain": llm_prediction_Domain,
        "Resouces": llm_prediction_Resouces,
        "Deliverables": llm_prediction_Deliverables,
        "designations": llm_prediction_designations,
        "skill": llm_prediction_skill,
        "Outcome": llm_prediction_Outcome
    }

    file_result_methods.create_file_llm_result(predictions)

    return predictions

@router.get("/files")
async def file_list():
    files = file_result_methods.fetch_file_list()
    return {"message": "Show all files", "files": files}

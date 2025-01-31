from fastapi import FastAPI
from pydantic import BaseModel
from typing import Dict

app = FastAPI()

# Sample data: Predefined message templates
TEMPLATES = {
    "missed_payment_1": "Dear customer, we noticed a missed payment on your policy. Please contact us ASAP to resolve this.",
    "missed_payment_2": "This is a second reminder about your missed payment. Please reach out to avoid policy cancellation.",
    "cancellation_notice": "Your policy has been canceled due to non-payment. Contact us to discuss reinstatement options."
}

class TemplateRequest(BaseModel):
    key: str

@app.get("/templates/")
def get_templates():
    """Returns all available message templates."""
    return {"templates": list(TEMPLATES.keys())}

@app.post("/template/")
def get_template(request: TemplateRequest):
    """Fetches a message template based on the key."""
    message = TEMPLATES.get(request.key, "Template not found.")
    return {"message": message}

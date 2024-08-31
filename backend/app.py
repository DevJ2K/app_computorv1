from fastapi import FastAPI, status, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import logging
import sys
import os
import time

# Import my package
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'computorv1')))
from computorv1.Computor import Computor
from computorv1.ErrorManager import *

logging.basicConfig(level=logging.DEBUG,
					filename="api.log",
					filemode="a",
					format='%(asctime)s - %(levelname)s - %(message)s')

class Polynomial(BaseModel):
	content: str

app = FastAPI()

app.add_middleware(
	CORSMiddleware,
	allow_origins=["*"],
	allow_credentials=True,
	allow_methods=["*"],
	allow_headers=["*"],
)

# @app.get("/")
# async def root():
# 	return {
# 		"message": "API is working !"
# 	}

@app.post("/solve", status_code=status.HTTP_200_OK)
async def solve(body: Polynomial) -> dict:
	polynomial = body.content
	from computorv1 import ErrorManager
	try:
		logging.info(f"Polynomial provided by client : '{polynomial}'")
		computor = Computor(polynomial)
		logging.info(f"Polynomial has been solved successfully !")
		return computor.get_solution()
	except Exception as e:
		exception_name = type(e).__name__
		if exception_name == "InvalidPolynomialError":
				logging.error("The provided polynomial is invalid. Please check the format and try again.")
				raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="The provided polynomial is invalid. Please check the format and try again.")
		elif exception_name == "MonomialError":
			logging.error("There is an issue with one or more monomials in the polynomial. Please review and correct them.")
			raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="There is an issue with one or more monomials in the polynomial. Please review and correct them.")
		elif exception_name == "MonomialConvertError":
			logging.error("Could not convert one or more monomials. Ensure that the polynomial is properly formatted.")
			raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Could not convert one or more monomials. Ensure that the polynomial is properly formatted.")
		else:
			raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Internal error due to a bad request.")



# curl -s -H 'Content-Type: application/json' -d '{ "name":"3x + 1 = 0"}' -X POST http://127.0.0.1:8000/test/ | jq
if __name__ == "__main__":
	computor = Computor("3x = 4x")
	computor.display_solution()

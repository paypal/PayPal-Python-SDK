from paypalrestsdk import Authorization

import logging
logging.basicConfig(level=logging.INFO)

authorization = Authorization.find("7GH53639GA425732B")

authorization.amount = {
  "currency": "USD",
  "total": "7.00" }

if authorization.reauthorize():
  print("Reauthorized[%s] successfully"%(authorization.id))
else:
  print(authorization.error)

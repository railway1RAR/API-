from fastapi import FastAPI, Request,Response

app = FastAPI()

# @app.get("/example")
# def read_example_headers(request: Request):
#     headers = request.headers
#     # Access specific header values
#     user_agent = headers.get("user-agent")
#     authorization = headers.get("authorization")
#     custom_header = headers.get("custom-header")

#     return {
#         "User-Agent": user_agent,
#         "Authorization": authorization,
#         "Custom-Header": custom_header
#     }
@app.get("/example")
def example_endpoint():
    content = "Hello, this is the response content."

    # Create a Response object and set custom headers
    response = Response(content=content)
    response.headers["X-Custom-Header"] = "This is custom value"
    response.headers["Authorization"] = "pass_token_1234"

    return response
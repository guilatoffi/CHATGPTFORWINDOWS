from mitmproxy import http

def request(flow: http.HTTPFlow) -> None:
    if "chatgpt.com/backend-api/me" in flow.request.pretty_url:
        # Do nothing and effectively drop the request without sending any response
        flow.response = http.Response.make(500, b"", {})  # Optional: Send an empty response
        flow.response._content = None  # Make sure there’s no response content
        flow.response.headers = {}  # Clear headers if needed

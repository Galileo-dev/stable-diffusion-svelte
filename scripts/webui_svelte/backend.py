
import os
from pydantic import BaseModel
from fastapi import HTTPException, FastAPI, Response, Depends, Request
from starlette.websockets import WebSocket, WebSocketState
from uuid import UUID, uuid4
from typing import List, Optional
import mimetypes
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse, RedirectResponse, FileResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi import Depends, FastAPI
from fastapi.security import OAuth2PasswordBearer
import uvicorn

from PIL import ImageChops

mimetypes.init()
mimetypes.add_type('application/javascript', '.js')







app = FastAPI()

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/create_session/{name}")
async def create_session(name: str, response: Response):

    return f"created session for {name}"


@app.get("/user")
@app.get("/user/")
def get_current_user(request: Request) -> Optional[str]:
    token = request.cookies.get("access-token")
    return 1


@app.get("/whoami")
async def whoami():
    pass


@app.post("/delete_session")
async def del_session(response: Response):
   pass


@app.get("/static/{path:path}")
def static_resource(path: str):
    static_file = safe_join(os.path.join(
        os.getcwd(), './frontend/public'), path)
    if static_file is not None:
        return FileResponse(static_file)
    raise HTTPException(status_code=404, detail="Static file not found")


templates = Jinja2Templates(directory="./frontend/public")


class Txt2ImgRequest(BaseModel):
    orig_width: int
    orig_height: int

    prompt: Optional[str]
    negative_prompt: Optional[str]
    sampler_name: Optional[str]
    steps: Optional[int]
    cfg_scale: Optional[float]

    batch_count: Optional[int]
    batch_size: Optional[int]
    base_size: Optional[int]
    max_size: Optional[int]
    seed: Optional[str]
    tiling: Optional[bool]

    use_gfpgan: Optional[bool]




@app.post("/txt2img")
async def txt2img_parser(req):
    pass
   

@app.head("/", response_class=HTMLResponse)
@app.get("/", response_class=HTMLResponse)
def main(request: Request):
    mimetypes.add_type("application/javascript", ".js")
    return templates.TemplateResponse("index_prod.html", {"request": request, "id": id})


def main():
    uvicorn.run("webui_svelte:app", host="localhost",
                port=8000, log_level="info")


if __name__ == "__main__":
    main()

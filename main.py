from datetime import datetime, timezone
from typing import Optional

import uvicorn

from fastapi import FastAPI, HTTPException, Response, Query, Path, Header
from starlette.responses import RedirectResponse

app = FastAPI(debug=True)

@app.get('/', include_in_schema=False)
def root():
    return RedirectResponse("/docs")


@app.get('/user_info/{user_id}/')
def find_user(
        user_id: int = Path(..., description="Ідентифікатор користувача"),
        timestamp: Optional[str] = Query(None, description="Мітка часу"),
        x_client_version: str = Header(..., description="Версія вашого клієнтського додатку")
):
    if not timestamp:
        timestamp = datetime.now(timezone.utc).astimezone().isoformat()

    return {
        "Welcome": f"Hello, user {user_id}!",
        "user_id": user_id,
        "timestamp": timestamp,
        "X-Client-Version": x_client_version
    }


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)

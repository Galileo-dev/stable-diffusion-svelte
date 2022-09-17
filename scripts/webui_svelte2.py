import uvicorn
# import modules

def main():
    uvicorn.run("backend:app", host="localhost",
                port=8000, log_level="info", app_dir="./scripts/webui_svelte", reload=True)


if __name__ == "__main__":
    main()

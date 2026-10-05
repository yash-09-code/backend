from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .core.config import get_settings
from .routers import (
    auth,
    profile,
    shops,
    members,
    categories,
    products,
    suppliers,
    sales,
    purchases,
    expenses,
    salaries,
    inventory,
    dashboard,
)

settings = get_settings()

app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    description="Business Management System API backed by Supabase Auth + Postgres/RLS.",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_list,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

prefix = settings.api_prefix

app.include_router(auth.router, prefix=prefix)
app.include_router(profile.router, prefix=prefix)
app.include_router(shops.router, prefix=prefix)
app.include_router(members.router, prefix=prefix)
app.include_router(categories.router, prefix=prefix)
app.include_router(products.router, prefix=prefix)
app.include_router(suppliers.router, prefix=prefix)
app.include_router(sales.router, prefix=prefix)
app.include_router(purchases.router, prefix=prefix)
app.include_router(expenses.router, prefix=prefix)
app.include_router(salaries.router, prefix=prefix)
app.include_router(inventory.router, prefix=prefix)
app.include_router(dashboard.router, prefix=prefix)


@app.get("/health", tags=["System"])
def health():
    return {
        "status": "ok",
        "service": settings.app_name,
        "version": settings.app_version,
    }

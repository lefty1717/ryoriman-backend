from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from uvicorn import run

from configuration import core_setting as CoreSetting

from router.ingredient_router import router as IngredientRouter
from router.recipe_router import router as RecipeRouter
from router.user_router import router as UserRouter
from router.user.fridge_router import router as FridgeRouter
from router.user.shoppingList_router import router as ShoppingListRouter



def create_application() -> FastAPI:
    application = FastAPI(
        docs_url=CoreSetting.DOCS_URL,
        redoc_url=CoreSetting.REDOC_URL,
        openapi_url=CoreSetting.OPENAPI_URL 
    )

    application.include_router(UserRouter)
    application.include_router(IngredientRouter)
    application.include_router(RecipeRouter)
    application.include_router(FridgeRouter)
    application.include_router(ShoppingListRouter)

    return application

app = create_application()

if __name__ == '__main__':
    run('main:app', host=CoreSetting.HOST, port=CoreSetting.PORT, reload=True)
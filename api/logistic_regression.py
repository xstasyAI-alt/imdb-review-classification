from fastapi import APIRouter

from src.logistic_regression import LogisticRegression

router = APIRouter()
logistic_regression = LogisticRegression()


@router.get("/logistic_regression")
async def logistic_regression_text_classifier(text: str):
    if text:
        predictions = logistic_regression.predict(input_text=text)

        return {
            "text": text,
            "predictions": {
                "label": str(predictions[0]),
                "prob_negative": float(predictions[1][0]),
                "prob_positive": float(predictions[1][1])
            }
        }

    raise ValueError("Must be a string!")

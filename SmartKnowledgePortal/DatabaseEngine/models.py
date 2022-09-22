from django.db import models

# Create your models here.
"""
Smart Portal Central Database Schema:

Developed : Vivek Vijayan
Recently : 22 -09 -2022

"""

"""////////////////////////////////// KNOWLEDGE HUB LINKS TABLE ////////////////////////////////////////"""

# Link Category table
class LinkCategory(models.Model):
    LinkCategoryID = models.BigAutoField(primary_key=True)
    LinkCategoryDescription = models.CharField(max_length=500)

    def __str__(self) -> str:
        return str(self.LinkCategoryDescription)


# Table for recording all the KH On boarding related links
class KH_OnboardingLinks(models.Model):
    KH_OnboardingLinksID = models.BigAutoField(primary_key=True)
    KH_OnboardingLinksTopic = models.CharField(
        max_length=500, default="Onboarding Topic"
    )
    KH_OnboardingLinksCategory = models.ForeignKey(
        LinkCategory, on_delete=models.CASCADE
    )
    KH_OnboardingLinksURL = models.URLField()

    def __str__(self) -> str:
        return (
            str(self.KH_OnboardingLinksID)
            + " - "
            + str(self.KH_OnboardingLinksTopic)
            + " : "
            + str(self.KH_OnboardingLinksURL)
        )


# Training links table
class KH_TrainingLinks(models.Model):
    KH_TrainingLinksID = models.BigAutoField(primary_key=True)
    KH_TrainingLinksDescription = models.CharField(
        max_length=500, default="Training Links"
    )
    KH_TrainingLinksCategory = models.ForeignKey(LinkCategory, on_delete=models.CASCADE)
    KH_TrainingLinksURL = models.URLField()

    def __str__(self) -> str:
        return (
            str(self.KH_TrainingLinksID)
            + " - "
            + str(self.KH_TrainingLinksDescription)
            + " : "
            + str(self.KH_TrainingLinksURL)
        )


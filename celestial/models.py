from django.db import models


# Create your models here.
class Star(models.Model):
    name = models.CharField(max_length=255)
    light_years_from_current = models.FloatField()


class Planet(models.Model):
    star = models.ForeignKey(Star, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    resources = models.ManyToManyField("Resource")


class Moon(models.Model):
    planet = models.ForeignKey(Planet, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    resources = models.ManyToManyField("Resource")


class Resource(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()


def search_resources(resource_name):
    planets_with_resource = Planet.objects.filter(
        resources__name=resource_name
    ).order_by("star__light_years_from_current")[:5]
    moons_with_resource = Moon.objects.filter(resources__name=resource_name).order_by(
        "planet__star__light_years_from_current"
    )[:5]

    # Merge and sort the two lists by distance and slice the result for the top 5
    combined = sorted(
        list(planets_with_resource) + list(moons_with_resource),
        key=lambda obj: obj.star.light_years_from_current
        if isinstance(obj, Planet)
        else obj.planet.star.light_years_from_current,
    )[:5]

    return combined

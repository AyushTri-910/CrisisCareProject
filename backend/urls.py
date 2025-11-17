from django.contrib import admin
from django.urls import path
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # --- EXISTING: LISTS (For the Dashboard) ---
    path('api/volunteers/', views.volunteer_list),
    path('api/disasters/', views.disaster_list),
    path('api/materials/', views.material_list),

    # --- NEW: DETAILS (For Deleting Specific Items) ---
    # These are the lines likely missing or incorrect!
    path('api/volunteers/<int:pk>/', views.volunteer_detail),
    path('api/disasters/<int:pk>/', views.disaster_detail),
    path('api/materials/<int:pk>/', views.material_detail),
]
from django.contrib import admin
from .models.award import Award, AwardTransaction
from .models.challenge import Challenge, ChallengeItem, ChallengeTransaction
from .models.user import User

# Register Award models
@admin.register(Award)
class AwardAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)

@admin.register(AwardTransaction)
class AwardTransactionAdmin(admin.ModelAdmin):
    list_display = ('award', 'user', 'created_at')
    search_fields = ('award__name', 'user__username')
    list_filter = ('created_at',)

# Register Challenge models
@admin.register(Challenge)
class ChallengeAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'point', 'award')
    search_fields = ('title', 'award__name')

@admin.register(ChallengeItem)
class ChallengeItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'challenge', 'description', 'date_to_display')
    search_fields = ('title', 'challenge__title')
    list_filter = ('date_to_display',)

@admin.register(ChallengeTransaction)
class ChallengeTransactionAdmin(admin.ModelAdmin):
    list_display = ('challenge_item', 'user', 'created_at', 'updated_at')
    search_fields = ('challenge_item__title', 'user__username')
    list_filter = ('created_at', 'updated_at')

# Register User model
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'birth_date', 'point_earned')
    search_fields = ('username', 'email')
    list_filter = ('birth_date',)

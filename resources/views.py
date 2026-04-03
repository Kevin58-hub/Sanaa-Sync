from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages  # Added for user feedback
from .models import Gig, GigApplication

def gig_list(request):
    # Only show gigs that are currently open for applications
    active_gigs = Gig.objects.filter(is_open=True).order_by('event_date')
    return render(request, 'resources/gig_list.html', {'gigs': active_gigs})

@login_required # Only logged-in artists can apply
def apply_for_gig(request, gig_id):
    gig = get_object_or_404(Gig, id=gig_id)
    
    # --- THE VETTING GATE (BACKEND SECURITY) ---
    if not request.user.is_vetted:
        messages.warning(request, f"Access Denied. Your profile must be vetted to apply for '{gig.title}'.")
        return redirect('gig_list')
    
    if request.method == 'POST':
        # Check if they already applied to prevent double submissions
        already_applied = GigApplication.objects.filter(gig=gig, artist=request.user).exists()
        
        if already_applied:
            messages.info(request, "You have already submitted an application for this gig.")
            return redirect('profile')

        # Create the application linked to the logged-in user
        GigApplication.objects.create(
            gig=gig,
            artist=request.user,
            message=request.POST.get('message', '')
        )
        
        messages.success(request, f"Success! Your application for {gig.title} has been sent.")
        return redirect('profile') # Redirect to profile to see the application status
    
    return render(request, 'resources/apply_confirm.html', {'gig': gig})
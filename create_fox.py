import pygame

# Create a simple fox image
size = (200, 200)
surface = pygame.Surface(size, pygame.SRCALPHA)
surface.fill((255, 255, 255, 255))  # White background

# Draw fox body (orange circle)
pygame.draw.circle(surface, (255, 140, 0), (100, 130), 50)

# Draw fox head (orange circle)
pygame.draw.circle(surface, (255, 140, 0), (100, 80), 40)

# Draw ears (triangles)
pygame.draw.polygon(surface, (255, 140, 0), [(70, 60), (80, 40), (90, 60)])
pygame.draw.polygon(surface, (255, 140, 0), [(110, 60), (120, 40), (130, 60)])

# Draw eyes
pygame.draw.circle(surface, (0, 0, 0), (85, 75), 5)
pygame.draw.circle(surface, (0, 0, 0), (115, 75), 5)

# Draw nose
pygame.draw.circle(surface, (0, 0, 0), (100, 90), 4)

# Draw tail
pygame.draw.ellipse(surface, (255, 140, 0), (140, 120, 40, 60))

# Add white tip to tail
pygame.draw.ellipse(surface, (255, 255, 255), (155, 155, 20, 20))

# Save
pygame.image.save(surface, "assets/images/family_fox.png")
print("Fox image created successfully!")

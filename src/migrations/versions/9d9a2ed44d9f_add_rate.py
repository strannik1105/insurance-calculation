"""Add Rate

Revision ID: 9d9a2ed44d9f
Revises: 
Create Date: 2024-12-01 20:31:15.445523

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "9d9a2ed44d9f"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.execute("CREATE SCHEMA insurance")
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "insurance_rate",
        sa.Column("cargo_type", sa.String(), nullable=False),
        sa.Column("rate", sa.Float(), nullable=False),
        sa.Column("transportation_date", sa.DateTime(), nullable=False),
        sa.Column("sid", sa.UUID(), nullable=False),
        sa.PrimaryKeyConstraint("sid"),
        schema="insurance",
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("insurance_rate", schema="insurance")
    # ### end Alembic commands ###
    op.execute("DROP SCHEMA insurance")
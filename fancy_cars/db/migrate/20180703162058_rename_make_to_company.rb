class RenameMakeToCompany < ActiveRecord::Migration[5.1]
  def change
    rename_column :cars, :make, :company
  end
end
